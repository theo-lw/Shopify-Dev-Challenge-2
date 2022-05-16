SERVER = "https://Shopify-Dev-Challenge-1.theo-lw.repl.co"
  
async function submit_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#create_inventory");
  const data = {
    name: form.querySelector('input[name="name"]').value
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
    alert("Inventory failed to be created");
  }
}
  
document.querySelector("#create_inventory").onsubmit = submit_inventory;  

async function view_inventory(e) {
  e.preventDefault();
  const response = await fetch(`${SERVER}/inventory/all`, {
    method: 'GET'
  });

  if (!response.ok) {
    alert("Cannot view inventory!");
  }

  const json = await response.json();
  document.querySelector("#inventory").innerHTML = JSON.stringify(json, null, 4);
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
    alert("Inventory failed to be deleted");
  }
}
  
document.querySelector("#delete_inventory").onsubmit = remove_inventory; 

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
    alert("Inventory failed to be deleted");
  }
}
  
document.querySelector("#delete_inventory").onsubmit = remove_inventory;  

async function change_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#edit_inventory");
  const data = {
    id: form.querySelector('input[name="id"]').value,
    name: form.querySelector('input[name="name"]').value,
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
    alert("Inventory failed to be edited");
  }
}
  
document.querySelector("#edit_inventory").onsubmit = change_inventory; 

async function submit_warehouse(e) {
  e.preventDefault();
  const form = document.querySelector("#create_warehouse");
  const data = {
    name: form.querySelector('input[name="name"]').value
  };

  const response = await fetch(`${SERVER}/warehouse/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Warehouse created successfully");
  } else {
    alert("Warehouse failed to be created");
  }
}
  
document.querySelector("#create_warehouse").onsubmit = submit_warehouse; 

async function view_warehouse(e) {
  e.preventDefault();
  const response = await fetch(`${SERVER}/warehouse/all`, {
    method: 'GET'
  });

  if (!response.ok) {
    alert("Cannot view warehouses!");
  }

  const json = await response.json();
  document.querySelector("#warehouses").innerHTML = JSON.stringify(json, null, 4);
}

document.querySelector("#view_warehouses").onclick = view_warehouse;

async function view_warehouse_for_inventory(e) {
  e.preventDefault();
  const form = document.querySelector("#warehouses_inventory");
  const id = form.querySelector('input[name="id"]').value;
  
  const response = await fetch(`${SERVER}/inventory/${id}/warehouse`, {
    method: 'GET',
  });

  if (!response.ok) {
    alert("Cannot view warehouse for inventory!");
  }

  const json = await response.json();
  document.querySelector("#warehouses_for_inventory").innerHTML = JSON.stringify(json, null, 4);
}

document.querySelector("#warehouses_inventory").onsubmit = view_warehouse_for_inventory;

async function assign_to_warehouse(e) {
  e.preventDefault();
  const form = document.querySelector("#assign_inventory");
  const data = {
    inventory_id: form.querySelector('input[name="inventory_id"]').value,
    warehouse_id: form.querySelector('input[name="warehouse_id"]').value,
    count: form.querySelector('input[name="count"]').value,
  };

  const response = await fetch(`${SERVER}/inventory/assign_to_warehouse`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  if (response.ok) {
    alert("Inventory assigned to warehouse successfully");
  } else {
    alert("Inventory failed to be assigned to warehouse");
  }
}
  
document.querySelector("#assign_inventory").onsubmit = assign_to_warehouse; 