<template>
  <div>
    <header>
      <div class="header-content">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" />
        <nav>
          <ul>
            <li>
              <RouterLink to="/">Home</RouterLink>
            </li>
            <li>
              <RouterLink to="/scoreboard-page">Scores</RouterLink>
            </li>
            <li>
              <RouterLink to="/admin">Admin</RouterLink>
            </li>
            <li>
              <RouterLink to="/about">About</RouterLink>
            </li>
          </ul>
        </nav>
      </div>
    </header>

    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
header {
  background-color: transparent;
  backdrop-filter: blur(5px);
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.logo {
  display: block;
  width: 7%;
  height: 100%;
  max-height: 3rem;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  padding-right: 3rem;
}

nav li {
  margin-left: 2.5rem;
  list-style: none;
}

nav a {
  color: rgb(255, 255, 255);
  text-decoration: none;
  font-size: 2rem;
  letter-spacing: 1px;
}

nav a:hover {
  background: #41d215;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

@media (max-width: 768px) {
  .header-content {
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    padding: 0.5rem;
  }

  nav ul {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0;
    margin-top: 1rem;
  }

  nav li {
    margin: 0 0.5rem;
  }
  nav a::before {
    bottom: -0.7em;
  }
}
</style>
