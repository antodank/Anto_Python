function checkInt([int] $value){
if(isInt($value) -eq $true){
	write-output "Valid"
}else{
	write-output "Invalid" 
}
}

function isInt([int] $value)
{
	$valid = $false
	if($value -match "^[0-9]+$"){
		$valid = $true
	}
	return $valid
}

checkInt $value