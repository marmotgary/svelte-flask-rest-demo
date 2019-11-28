<script>
  import {link} from 'svelte-spa-router'
  import { onMount } from 'svelte';
  export let params = {};
  let pkg;
  // let url =
  // console.log(params.wild)
  let url = 'http://localhost:5001/api/v1/package/' + params.wild;
  onMount(async () => {
    const res = await fetch(url);
    pkg = await res.json();
  });
  function getPackage(event) {
    console.log(event);
  }
</script>
{#if pkg}
    <p><span>Name:</span> {pkg.name}</p>
    <p><span>Description short:</span> {pkg.description_short}</p>
    <p><span>Description:</span> {@html pkg.description}</p>
    <p><span>This depends on:</span>
        {#each pkg.depends as pkg}
        <span class="dependList">
          {#if pkg.id != null}
                <a on:click={getPackage} class="dependList" href="/package/{pkg.id}" use:link>{pkg.name}</a>
            {:else}
                <span style="color: black; font-weight: 400;">{pkg.name}</span>
            {/if}
        </span>
        {/each}
    </p>
    <p><span>Depends on this:</span>
        {#each pkg.depends_this as pkg}
        <span class="dependList">
          {#if pkg.id != null}
                <a on:click={getPackage} class="dependList" href="/package/{pkg.id}" use:link>{pkg.name}</a>
            {:else}
                <span style="color: black; font-weight: 400;">{pkg.name}</span>
            {/if}
        </span>
        {/each}
    </p>
{/if}

<style>
  span {
    color: #ff3e00;
    font-weight: 500;
  }
  .dependList::after{
    content: " | ";
  }
  .dependList:last-child::after{
    content: "";
  }
</style>
