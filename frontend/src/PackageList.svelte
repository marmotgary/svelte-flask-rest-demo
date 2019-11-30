<script>
  import LoadingSpinner from './LoadingSpinner.svelte';
  import {onMount} from 'svelte';

  let packages = [];
  onMount(async () => {
    const res = await fetch('http://localhost:5001/api/v1/packages');
    packages = await res.json();
  })
</script>
<div id="packageContainer">
    {#each packages as pkg}
      <li>
        <a href="#/package/{pkg.id}">
            {pkg.name}
        </a>
      </li>
    {:else}
      <LoadingSpinner/>
    {/each}
</div>

<style>
  li {
    list-style-type: none;
  }

</style>
