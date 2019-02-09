function reverseString(string) {
  let wordArray = string.split('');
  let alphanumericChars = [];
  for (i = 0; i < wordArray.length; i++) {
    if (wordArray[i].match(/[a-zA-Z0-9]/)) {
      alphanumericChars.push(wordArray[i]);
      wordArray[i] = "";
    }
  }
  for (i = 0; i < wordArray.length; i++) {
    if (wordArray[i] == ""){
      wordArray[i] = alphanumericChars.splice(-1, 1);
    }
  }
  console.log(wordArray.join(''))
}

reverseString("!!aP ples_Ar3__G r8!")