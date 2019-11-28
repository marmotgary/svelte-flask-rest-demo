<script>
  import DepenencyList from "./DepenencyList.svelte";
  import LoadingSpinner from './LoadingSpinner.svelte';
  export let params;
  let pkg, url;
  let fetching = false;
  // Fetch package from API each time url changes
  $: {
    let url = 'http://localhost:5001/api/v1/package/' + params.id;
    fetching = true;
    console.log(url);
    getPackages(url);
  }

  async function getPackages(url) {
    const res = await fetch(url);
    pkg = await res.json();
    fetching = false;
  }

</script>
{#if pkg}
    <p><span>Name:</span> {pkg.name}</p>
    <p><span>Description short:</span> {pkg.description_short}</p>
    <p><span>Description:</span> {@html pkg.description}</p>
    <p><span>This depends on:</span>
        <DepenencyList packageList={pkg.depends}/>
    </p>
    <p><span>Depends on this:</span>
        <DepenencyList packageList={pkg.depends_this}/>
    </p>
{:else}
    <LoadingSpinner/>
{/if}
{#if fetching && pkg}
    <LoadingSpinner/>
{/if}
<style>
  span {
    color: #ff3e00;
    font-weight: 500;
  }
</style>
