$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$dataRoot = Join-Path $root 'mentor-database-recovery-2026-09-05/data'
$books = @(Get-Content -Raw (Join-Path $dataRoot 'books.json') | ConvertFrom-Json)
$writing = @(Get-Content -Raw (Join-Path $dataRoot 'writing_trait_annotations.json') | ConvertFrom-Json)
$reading = @(Get-Content -Raw (Join-Path $dataRoot 'reading_strategy_annotations.json') | ConvertFrom-Json)
$rows = foreach ($book in $books) {
    $w = @($writing | Where-Object book_id -eq $book.id)
    $r = @($reading | Where-Object book_id -eq $book.id)
    $wn = @($w | Where-Object { -not [string]::IsNullOrWhiteSpace($_.in_this_book_text) })
    $rn = @($r | Where-Object { -not [string]::IsNullOrWhiteSpace($_.in_this_book_text) })
    $queue = if ($w.Count -eq 0 -and $r.Count -eq 0) {'First writing/reading gap pass'} elseif ($r.Count -eq 0) {'Preserve writing; later reading review'} else {'Preserve tags; check explanation quality'}
    [pscustomobject]@{
        Book_ID = $book.id; Title = $book.title; Author = $book.author
        Writing_tags = $w.Count; Writing_notes_present = $wn.Count; Writing_notes_missing = $w.Count - $wn.Count
        Reading_tags = $r.Count; Reading_notes_present = $rn.Count; Reading_notes_missing = $r.Count - $rn.Count
        Work_queue = $queue; Blurb_status = $book.blurb_status
        PRIDE = 'Not yet assessed'; Inquiry = 'Not yet assessed'; Teaching_ideas = 'Not yet drafted'
        Notes = 'Based on recovered snapshot; note presence does not establish quality or approval.'
    }
}
if ($rows.Count -ne 343) { throw 'Unexpected book count' }
$rows | Export-Csv -LiteralPath (Join-Path $PSScriptRoot 'BOOK-CONTENT-GAPS.csv') -NoTypeInformation -Encoding utf8BOM
$rows | Group-Object Work_queue | Select-Object Name,Count | ConvertTo-Json
[pscustomobject]@{WritingNotesMissing=($rows|Measure-Object Writing_notes_missing -Sum).Sum;ReadingNotesMissing=($rows|Measure-Object Reading_notes_missing -Sum).Sum} | ConvertTo-Json
