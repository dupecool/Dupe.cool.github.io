document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    const grid = document.getElementById('tile-grid');
    if (grid) {
        function createGrid() {
            grid.innerHTML = '';

            const tileSize = 60;
            const columns = Math.ceil(window.innerWidth / tileSize);
            const rows = Math.ceil(window.innerHeight / tileSize);

            grid.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;

            const totalTiles = columns * rows;
            const maxTiles = 2500;
            const finalCount = Math.min(totalTiles, maxTiles);

            const fragment = document.createDocumentFragment();
            for (let i = 0; i < finalCount; i++) {
                const tile = document.createElement('div');
                tile.classList.add('tile');
                fragment.appendChild(tile);
            }
            grid.appendChild(fragment);
        }

        window.addEventListener('resize', createGrid);
        createGrid();

        document.body.onmousemove = e => {
            const { clientX, clientY } = e;
            grid.style.setProperty('--mouse-x', `${clientX}px`);
            grid.style.setProperty('--mouse-y', `${clientY}px`);
        };
    }
});
