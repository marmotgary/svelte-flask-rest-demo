<script>
  import {link} from 'svelte-spa-router'
  // import Package from './Package.svelte';
  import { onMount } from 'svelte';
  // const routes = {
  //   '/package/*': Package,
  // }
  // Put packages into store?
  let packages = [];
  onMount(async () => {
    const res = await fetch('http://localhost:5001/api/v1/packages');
    packages = await res.json();
  });
</script>
<!--<Router {routes}/>-->
<div id="packageContainer">
  {#each packages as pkg}
    <li>
      <a href="/package/{pkg.id}" use:link>
        {pkg.name}
      </a>
    </li>
  {:else}
    <p>...</p>
  {/each}
</div>

<style>
  li {
    list-style-type: none;
  }

</style>
