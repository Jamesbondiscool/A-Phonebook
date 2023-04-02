// Phonebook array to store contacts
let phonebook = [];

// Add contact function
function addContact() {
  let name = prompt("Enter name:");
  let phone = prompt("Enter phone number:");
  let contact = { name: name, phone: phone };
  phonebook.push(contact);
  playSound()
}

// Display phonebook function
function displayPhonebook() {
  let tableBody = document.getElementById("table-body");
  tableBody.innerHTML = "";
  phonebook.forEach(function(contact, index) {
    let row = `<tr>
                  <td>${index + 1}</td>
                  <td>${contact.name}</td>
                  <td>${contact.phone}</td>
                  <td class="actions">
                    <button onclick="editContact(${index})">Edit</button>
                    <button onclick="deleteContact(${index})">Delete</button>
                  </td>
                </tr>`;
    tableBody.innerHTML += row;
  });
}

// Search contact function
function searchContact() {
  let searchValue = document.getElementById("search-input").value.toLowerCase();
  let filteredContacts = phonebook.filter(function(contact) {
    return contact.name.toLowerCase().includes(searchValue) || contact.phone.includes(searchValue);
  });
  phonebook = filteredContacts;
  displayPhonebook();
}

// Edit contact function
function editContact(index) {
  let name = prompt("Enter new name:");
  let phone = prompt("Enter new phone number:");
  phonebook[index].name = name;
  phonebook[index].phone = phone;
  displayPhonebook();
}

// Delete contact function
function deleteContact(index) {
  phonebook.splice(index, 1);
  displayPhonebook();
}

// Event listeners
document.getElementById("add-btn").addEventListener("click", addContact);
document.getElementById("search-btn").addEventListener("click", searchContact);

// Play sound function
function playSound() {
  let audio = new Audio('drake_hotline_bling_lyrics_aac_45864.mp3');
  audio.play();
}

// Initial display
displayPhonebook();
