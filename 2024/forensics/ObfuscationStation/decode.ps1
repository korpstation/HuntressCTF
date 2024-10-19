$base64String = 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'

$decodedBytes = [Convert]::FromBase64String($base64String)
$memoryStream = New-Object IO.MemoryStream(,$decodedBytes)
$deflateStream = New-Object IO.Compression.DeflateStream($memoryStream, [IO.Compression.CompressionMode]::Decompress)
$reader = New-Object IO.StreamReader($deflateStream)

$decompressedString = $reader.ReadToEnd()
Write-Output $decompressedString

$reader.Close()
$deflateStream.Close()
$memoryStream.Close()
