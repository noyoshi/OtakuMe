
Text = document.getElementById("textarea1");
Label = document.getElementById("formLabel");
Form = document.getElementById("form");

btnSubmit = document.getElementById("submit");

// Text.addEventListener("focus", function(){
//   Label.style.visibility="hidden";
// });
//
// Text.addEventListener("blur", function(){
//   if (Text.text === "") {
//     Label.style.visibility="visible";
//   }
// });

btnSubmit.addEventListener("click", function(){
  Form.submit();
})
