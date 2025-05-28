<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from "axios";

const orders = ref([]);
const lists = ref([]);
const clients = ref([]);
const vents = ref([]);
const groupedOrders = ref([]);
const loading = ref(false);

async function fetchOrders() {
  try {
    loading.value = true;
    const response = await axios.get("/api/orders/");
    orders.value = response.data;
    return response.data;
  } catch (error) {
    console.error('Error fetching orders:', error);
    return [];
  }
}

async function fetchLists() {
  try {
    const response = await axios.get("/api/lists/");
    lists.value = response.data;
    return response.data;
  } catch (error) {
    console.error('Error fetching lists:', error);
    return [];
  }
}

async function fetchClients() {
  try {
    const response = await axios.get("/api/clients/");
    clients.value = response.data;
    return response.data;
  } catch (error) {
    console.error('Error fetching clients:', error);
    return [];
  }
}

async function fetchVents() {
  try {
    const response = await axios.get("/api/vents/");
    vents.value = response.data;
    return response.data;
  } catch (error) {
    console.error('Error fetching vents:', error);
    return [];
  }
}

function enrichOrderData(orders, lists, clients, vents) {
  return orders.map(order => {
    // Находим клиента по user ID
    const client = clients.find(c => c.user === order.user) || {};
    
    // Находим элементы заказа
    const orderItems = lists.filter(item => item.orderNumber === order.id)
      .map(item => {
        // Находим название вентиляционного элемента
        const vent = vents.find(v => v.id === item.ventName) || {};
        return {
          ...item,
          ventName: vent.ventName || `Unknown (ID: ${item.ventName})`
        };
      });

    return {
      ...order,
      userName: client.name || `Unknown (ID: ${order.user})`,
      userEmail: client.email,
      userPhone: client.phone,
      items: orderItems
    };
  });
}

async function fetchAndProcessData() {
  try {
    loading.value = true;
    const [ordersData, listsData, clientsData, ventsData] = await Promise.all([
      fetchOrders(),
      fetchLists(),
      fetchClients(),
      fetchVents()
    ]);
    
    groupedOrders.value = enrichOrderData(ordersData, listsData, clientsData, ventsData);
    console.log('Processed orders:', groupedOrders.value);
  } catch (error) {
    console.error('Error processing data:', error);
  } finally {
    loading.value = false;
  }
}

async function onLoadClick() {
  await fetchAndProcessData();
}

onBeforeMount(async () => {
  await fetchAndProcessData();
});
</script>

<template>
  <div>
    <button @click="onLoadClick" :disabled="loading">
      {{ loading ? 'Loading...' : 'Load Data' }}
    </button>

    <div v-if="groupedOrders.length">
      <div v-for="order in groupedOrders" :key="order.id" class="order">
        <h3>Номер заказа #{{ order.orderNumber }}</h3>
        <p>ФИО: {{ order.userName }}</p>
        <p>Почта: {{ order.userEmail }}</p>
        <p>Телефон: {{ order.userPhone }}</p>
        <p>Дата: {{ order.date }}</p>
        <p>Комментарий: {{ order.comment }}</p>
        
        <h4>Items:</h4>
        <ul>
          <li v-for="item in order.items" :key="item.id">
            Заготовка: {{ item.ventName }}, 
            Характеристики: {{ item.param }}, 
            Количество: {{ item.quantity }}
          </li>
        </ul>
      </div>
    </div>

    <div v-else-if="!loading">
      No orders found
    </div>
  </div>
</template>

<style scoped>
.order {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
}

button {
  padding: 0.5rem 1rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 1rem;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  background-color: #fff;
  border: 1px solid #eee;
  border-radius: 4px;
}
</style>