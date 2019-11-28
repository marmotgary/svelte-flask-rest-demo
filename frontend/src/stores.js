import { readable } from 'svelte/store';

export const test = readable([].length, function start(set) {
	// let packages = [];
	set(getPackages());
	getPackages();
	 async function getPackages() {
		const res = await fetch('http://localhost:5001/api/v1/packages');
		return await res.json();
	  }
});
