<script>
  import DepenencyList from "./DepenencyList.svelte";
  import LoadingSpinner from './LoadingSpinner.svelte';

  export let params;
  let url;
  let pkg;
  let fetching = false;
  // Fetch package from API each time url changes
  $: {
    let url = 'http://localhost:5001/api/v1/package/' + params.id;
    fetching = true;
    pkg = getPackages(url);
  }

  async function getPackages(url) {
    const res = await fetch(url);
    const pkg = await res.json();
    fetching = false;
    if (res.ok) {
      return pkg;
    } else {
      throw new Error(pkg.message);
    }
  }

</script>
{#await pkg}
  <LoadingSpinner/>
{:then pkg}
  <p><span>Name:</span> {pkg.name}</p>
  <p><span>Description short:</span> {pkg.description_short}</p>
  <p><span>Description:</span> {@html pkg.description}</p>
  <p><span>This depends on:</span>
    <DepenencyList packageList={pkg.depends}/>
  </p>
  <p><span>Depends on this:</span>
    <DepenencyList packageList={pkg.depends_this}/>
  </p>
{:catch error}
  <p><span>Error: </span>{error.message}</p>
{/await}

<style>
  span {
    color: #ff3e00;
    font-weight: 500;
  }
</style>
