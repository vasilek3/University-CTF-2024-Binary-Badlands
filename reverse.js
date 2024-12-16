function decryptROT13(input){
return input.replace(/[A-Za-z]/g, function(char){
    return String.fromCharCode( char.charCodeAt(0) + (char.toUpperCase() <= "M" ? 13 : -13 ));
 })
}

console.log(decryptROT13("Znoyrf"))