SERVER = "https://Shopify-Dev-Challenge-2.theo-lw.repl.co"
  
async function submit_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#create_inventory");
  const data = {
    name: form.querySelector('input[name="name"]').value,
    city_id: form.querySelector('input[name="city_id"]').value,
  };

  const response = await fetch(`${SERVER}/inventory/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Inventory created successfully");
  } else {
    alert(`Inventory failed to be created: ${response.text}`);
  }
}
  
document.querySelector("#create_inventory").onsubmit = submit_inventory;  

async function view_inventory(e) {
  e.preventDefault();
  const response = await fetch(`${SERVER}/inventory/all`, {
    method: 'GET'
  });

  if (!response.ok) {
    alert(`Cannot view inventory! ${response.text}`);
  }

  const json = await response.json();
  document.querySelector("#inventory").innerHTML = "<pre>" +  JSON.stringify(json, null, '\t') + "</pre>";
}

document.querySelector("#view_inventory").onclick = view_inventory;

async function remove_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#delete_inventory");
  const data = {
    id: form.querySelector('input[name="id"]').value
  };

  const response = await fetch(`${SERVER}/inventory/delete`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Inventory deleted successfully");
  } else {
    alert(`Inventory failed to be deleted : ${response.text}`);
  }
}
  
document.querySelector("#delete_inventory").onsubmit = remove_inventory; 

async function change_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#edit_inventory");
  const data = {
    id: form.querySelector('input[name="id"]').value,
    name: form.querySelector('input[name="name"]').value,
    city_id: form.querySelector('input[name="city_id"]').value,
  };

  const response = await fetch(`${SERVER}/inventory/edit`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Inventory edited successfully");
  } else {
    alert(`Inventory failed to be edited: : ${response.text}`);
  }
}
  
document.querySelector("#edit_inventory").onsubmit = change_inventory; 

async function submit_city(e) {
  e.preventDefault();
  const form = document.querySelector("#create_city");
  const data = {
    name: form.querySelector('input[name="name"]').value,
    longitude: form.querySelector('input[name="longitude"]').value,
    latitude: form.querySelector('input[name="latitude"]').value,
  };

  const response = await fetch(`${SERVER}/city/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("City created successfully");
  } else {
    alert(`City failed to be created: : ${response.text}`);
  }
}
  
document.querySelector("#create_city").onsubmit = submit_city; 

async function view_city(e) {
  e.preventDefault();
  const response = await fetch(`${SERVER}/city/all`, {
    method: 'GET'
  });

  if (!response.ok) {
    alert(`Cannot view cities! ${response.text}`);
  }

  const json = await response.json();
  document.querySelector("#cities").innerHTML = "<pre>" + JSON.stringify(json, null, '\t') + "</pre>";
}

document.querySelector("#view_cities").onclick = view_city;