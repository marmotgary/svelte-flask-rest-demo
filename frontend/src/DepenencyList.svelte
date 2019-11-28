<script>
    export let packageList = null;
</script>

{#if packageList != null}
{#each packageList as pkg}
    <span class="dependList">
      {#if pkg.id != null}
            <a class="dependList" href="#/package/{pkg.id}">{pkg.name}</a>
        {:else}
            <span style="color: black; font-weight: 400;">{pkg.name}</span>
        {/if}
    </span>
{/each}
{/if}

<style>
  span {
    color: #ff3e00;
  }
  .dependList::after{
    content: " | ";
  }
  .dependList:last-child::after{
    content: "";
  }
</style>
