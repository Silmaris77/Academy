# Fix merge conflicts by removing all conflict markers
$files = Get-ChildItem -Recurse -Include "*.py" 

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # Remove conflict markers
    $content = $content -replace "<<<<<<< HEAD[^\r\n]*", ""
    $content = $content -replace ">>>>>>> explore-23158b6[^\r\n]*", ""
    $content = $content -replace "=======[^\r\n]*", ""
    
    # Clean up any resulting empty lines (optional)
    $content = $content -replace "(\r?\n){3,}", "`r`n`r`n"
    
    Set-Content $file.FullName $content -NoNewline
    Write-Host "Fixed: $($file.FullName)"
}

Write-Host "All merge conflicts fixed!"
