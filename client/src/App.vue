<script setup>

</script>

<template>
<div class="container main">
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand nav-link" href="/">ИРКТЕХ</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-between" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" to="/service">Услуги</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/vent">Заготовки</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/cart">Корзина</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/profile">Мой профиль</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Пользователь
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="/admin">Админка</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div>
    <router-view/>
  </div>
  <div class="footer row">
    <div class="col">
      Общество с ограниченной ответственностью «ИРКТЕХ»<br>
      Адрес: 664035, г. Иркутск, ул. Петрова д.17<br>
      Инв: 3808182080<br>
      ОГРН: 1153850045800
    </div>
    <div class="col cunt">
      Контакты:<br>
      Телефон: 88005553535<br>
      Почта: irktech00@mail.ru<br>
    </div>
  </div>
</div>
</template>

<style scoped>
.footer {
  margin-top: 40px;
  font-size: 14px;
  color: #666;
  line-height: 1.4;
  }
.cunt{
  display: flex; justify-content: right;
  }
</style>