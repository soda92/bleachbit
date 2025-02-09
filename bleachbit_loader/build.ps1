Copy-Item -Recurse -Force $PSScriptRoot/../bleachbit $PSScriptRoot
Copy-Item -Recurse -Force $PSScriptRoot/../data $PSScriptRoot
Copy-Item -Recurse -Force $PSScriptRoot/../cleaners $PSScriptRoot
Copy-Item -Recurse -Force $PSScriptRoot/../windows $PSScriptRoot

"111" > $PSScriptRoot/tmp.txt