<script>
  import Router, {link} from 'svelte-spa-router'
  import PackageList from './PackageList.svelte';
  import Package from './Package.svelte';
  import Header from './Header.svelte';
  const routes = {
    '/': PackageList,
    '/package/*': Package,
  }
</script>

<main>
  <Header/>
  <!--	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>-->
  <Router {routes}/>
<!--  <PackageList/>-->
</main>

<style>
  main {
    /*text-align: center;*/
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
