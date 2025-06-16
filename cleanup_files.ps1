# 🧹 SKRYPT CZYSZCZENIA ZENDEGENACADEMY
# Usuwa niepotrzebne pliki testowe, debugowe i tymczasowe

Write-Host "🧹 CZYSZCZENIE ZENDEGENACADEMY" -ForegroundColor Cyan
Write-Host "=" * 50 -ForegroundColor Cyan

# Sprawdź czy jesteśmy w prawidłowym katalogu
if (-not (Test-Path "main.py")) {
    Write-Host "❌ Błąd: Nie znaleziono main.py. Uruchom skrypt z katalogu ZenDegenAcademy" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Znaleziono main.py - kontynuujemy czyszczenie..." -ForegroundColor Green

# Funkcja do liczenia plików przed usunięciem
function Count-Files {
    param($pattern)
    $files = Get-ChildItem -Name $pattern -ErrorAction SilentlyContinue
    return $files.Count
}

# Funkcja do usuwania plików z raportowaniem
function Remove-FilesWithReport {
    param($pattern, $description)
    
    $files = Get-ChildItem -Name $pattern -ErrorAction SilentlyContinue
    $count = $files.Count
    
    if ($count -gt 0) {
        Write-Host "🗑️  Usuwanie $description ($count plików)..." -ForegroundColor Yellow
        foreach ($file in $files) {
            Write-Host "   - $file" -ForegroundColor DarkGray
        }
        Remove-Item $pattern -Force -ErrorAction SilentlyContinue
        Write-Host "✅ Usunięto $count plików: $description" -ForegroundColor Green
    } else {
        Write-Host "ℹ️  Brak plików do usunięcia: $description" -ForegroundColor Gray
    }
}

Write-Host "`n📊 ANALIZA PLIKÓW PRZED CZYSZCZENIEM:" -ForegroundColor Cyan

# Policz pliki przed czyszczeniem
$testFiles = Count-Files "test_*.py"
$debugFiles = Count-Files "debug_*.py"
$quickFiles = Count-Files "quick_*.py"
$simpleFiles = Count-Files "simple_*.py"
$verifyFiles = Count-Files "verify_*.py"
$validateFiles = Count-Files "validate_*.py"
$tempFiles = Count-Files "*_output.txt"
$resultFiles = Count-Files "*_result*.txt"
$logFiles = Count-Files "*.log"
$brokenFiles = Count-Files "*.broken"

$totalToRemove = $testFiles + $debugFiles + $quickFiles + $simpleFiles + $verifyFiles + $validateFiles + $tempFiles + $resultFiles + $logFiles + $brokenFiles

Write-Host "   Test files: $testFiles" -ForegroundColor Yellow
Write-Host "   Debug files: $debugFiles" -ForegroundColor Yellow
Write-Host "   Quick files: $quickFiles" -ForegroundColor Yellow
Write-Host "   Simple files: $simpleFiles" -ForegroundColor Yellow
Write-Host "   Verify files: $verifyFiles" -ForegroundColor Yellow
Write-Host "   Validate files: $validateFiles" -ForegroundColor Yellow
Write-Host "   Temp/output files: $($tempFiles + $resultFiles)" -ForegroundColor Yellow
Write-Host "   Log files: $logFiles" -ForegroundColor Yellow
Write-Host "   Broken files: $brokenFiles" -ForegroundColor Yellow
Write-Host "   🎯 ŁĄCZNIE DO USUNIĘCIA: $totalToRemove plików" -ForegroundColor Magenta

if ($totalToRemove -eq 0) {
    Write-Host "`n✨ Katalog jest już czysty! Brak plików do usunięcia." -ForegroundColor Green
    exit 0
}

# Pytaj użytkownika o zgodę
Write-Host "`n⚠️  UWAGA: Zamierzasz usunąć $totalToRemove plików!" -ForegroundColor Red
$response = Read-Host "Czy chcesz kontynuować? (y/N)"

if ($response -ne "y" -and $response -ne "Y") {
    Write-Host "❌ Anulowano czyszczenie." -ForegroundColor Red
    exit 0
}

Write-Host "`n🚀 ROZPOCZYNANIE CZYSZCZENIA..." -ForegroundColor Cyan

# Usuń pliki testowe
Remove-FilesWithReport "test_*.py" "pliki testowe (test_*.py)"
Remove-FilesWithReport "*_test.py" "pliki testowe (*_test.py)"

# Usuń pliki debugowe
Remove-FilesWithReport "debug_*.py" "pliki debugowe"

# Usuń pliki quick
Remove-FilesWithReport "quick_*.py" "pliki quick test"

# Usuń pliki simple
Remove-FilesWithReport "simple_*.py" "pliki simple test"

# Usuń pliki weryfikacyjne
Remove-FilesWithReport "verify_*.py" "pliki weryfikacyjne"
Remove-FilesWithReport "validate_*.py" "pliki walidacyjne"

# Usuń pliki tymczasowe
Remove-FilesWithReport "*_output.txt" "pliki wyjściowe"
Remove-FilesWithReport "*_result*.txt" "pliki wyników"
Remove-FilesWithReport "badge_award_results.txt" "wyniki przyznawania odznak"
Remove-FilesWithReport "verification_output.txt" "wyniki weryfikacji"

# Usuń logi
Remove-FilesWithReport "*.log" "pliki logów"

# Usuń złamane pliki
Remove-FilesWithReport "*.broken" "złamane pliki"

# Usuń skrypty PowerShell (opcjonalnie)
$psFiles = Get-ChildItem -Name "*.ps1" -ErrorAction SilentlyContinue
if ($psFiles.Count -gt 0) {
    Write-Host "`n🤔 Znaleziono skrypty PowerShell:" -ForegroundColor Yellow
    foreach ($file in $psFiles) {
        Write-Host "   - $file" -ForegroundColor DarkGray
    }
    $response = Read-Host "Czy usunąć skrypty PowerShell? (y/N)"
    if ($response -eq "y" -or $response -eq "Y") {
        Remove-FilesWithReport "*.ps1" "skrypty PowerShell"
    }
}

# Usuń pliki wsadowe
Remove-FilesWithReport "*.bat" "pliki wsadowe"

Write-Host "`n🎉 CZYSZCZENIE ZAKOŃCZONE!" -ForegroundColor Green

# Pokaż ile plików zostało
$remainingPython = (Get-ChildItem -Name "*.py").Count
$remainingTotal = (Get-ChildItem -File).Count

Write-Host "📊 PODSUMOWANIE:" -ForegroundColor Cyan
Write-Host "   Pozostałe pliki Python: $remainingPython" -ForegroundColor Green
Write-Host "   Wszystkie pozostałe pliki: $remainingTotal" -ForegroundColor Green
Write-Host "   Katalog jest teraz znacznie czystszy! ✨" -ForegroundColor Green

Write-Host "`n💡 ZALECENIA:" -ForegroundColor Cyan
Write-Host "   1. Uruchom aplikację aby sprawdzić czy wszystko działa" -ForegroundColor White
Write-Host "   2. Rozważ przeniesienie dokumentacji .md do folderu /docs/" -ForegroundColor White
Write-Host "   3. Sprawdź czy pliki HTML demo są jeszcze potrzebne" -ForegroundColor White
