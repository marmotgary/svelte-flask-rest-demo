<script>
  import Router from 'svelte-spa-router'
  import PackageList from './PackageList.svelte';
  import Package from './Package.svelte';
  import Header from './Header.svelte';
  const routes = {
    '/': PackageList,
    '/package/:id': Package,
  }
</script>

<main>
  <Header/>
  <Router {routes}/>
</main>

<style>
  main {
    padding: 1em;
    max-width: 1024px;
    margin: 0 auto;
  }

  @media (max-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
