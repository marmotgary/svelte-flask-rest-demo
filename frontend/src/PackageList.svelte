<script>
  import { onMount } from 'svelte';
  // Put packages into store?
  let packages = [];
  onMount(async () => {
    const res = await fetch('http://localhost:5001/api/v1/packages');
    packages = await res.json();
  });
</script>

{#each packages as pkg (pkg.id)}
  <li><a href="package/{pkg.id}">
      {pkg.name}
  </a></li>
{:else}
  <p>Loading...</p>
{/each}
