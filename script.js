
function generatePassword() {
  const length = parseInt(document.getElementById("length").value);
  const useUppercase = document.getElementById("uppercase").checked;
  const useNumbers = document.getElementById("numbers").checked;
  const useSymbols = document.getElementById("symbols").checked;

  let characters = "abcdefghijklmnopqrstuvwxyz";
  if (useUppercase) characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (useNumbers) characters += "0123456789";
  if (useSymbols) characters += "!@#$%^&*()-_=+[]{}<>?";

  if (characters.length === 0) {
    document.getElementById("result").innerText = "Please select at least one character type.";
    return;
  }

  let password = "";
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    password += characters[randomIndex];
  }

  document.getElementById("result").innerText = password;
}
