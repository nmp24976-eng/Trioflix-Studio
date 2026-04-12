// Dummy Data
const users = [
  { name: "Rahul", email: "rahul@example.com", status: "Active" },
  { name: "Priya", email: "priya@example.com", status: "Inactive" },
  { name: "Amit", email: "amit@example.com", status: "Active" },
   { name: "neraj", email: "neraj@example.com", status: "Active" }
];

// Select Table Body
const tableBody = document.querySelector('table tbody');

// Show Data in Table
function displayUsers(data) {
  console.log('Displaying users with data:', data); // Debug log
  tableBody.innerHTML = ''; // Clear existing data
  
  if (data.length === 0) {
      tableBody.innerHTML = '<tr><td colspan="3">No results found</td></tr>';
      return;
  }

  data.forEach(user => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${user.name}</td>
      <td>${user.email}</td>
      <td>${user.status}</td>
    `;
    tableBody.appendChild(row);
  });
}

// Initial Display
displayUsers(users);

// Search/Filter Functionality
const searchInput = document.getElementById('searchinput');

searchinput.addEventListener('keyup', function() {
  const query = this.value.toLowerCase();
  console.log('Search query:', query); // Debug log

  const filteredUsers = users.filter(user => 
    user.name.toLowerCase().includes(query) ||
    user.email.toLowerCase().includes(query) ||
    user.status.toLowerCase().includes(query)
  );
  
  console.log('Filtered users:', filteredUsers); // Debug log
  displayUsers(filteredUsers); // Update table with filtered data
});