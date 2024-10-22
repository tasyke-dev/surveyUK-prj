
var modal = document.getElementById('mobileModal');

// Get the button that opens the modal
var btn = document.getElementById('submitBtn');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

btn.addEventListener('click',openModal);

span.addEventListener('click',closeModal);

window.addEventListener('click',outsideClick);

// When the user clicks the button, open the modal 
function openModal() {
  modal.style.display = "block";
  console.log('aboba');
}

// When the user clicks on <span> (x), close the modal
function closeModal() {
  modal.style.display = "none";
  console.log('aboba');
}

// When the user clicks anywhere outside of the modal, close it
function outsideClick (event) {
  if (event.target == modal) {
    modal.style.display = "none";
    console.log('aboba');
  }
}