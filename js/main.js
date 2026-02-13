document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (window.lucide) {
        window.lucide.createIcons();
    }

    // Tile Grid Logic
    const grid = document.getElementById('tile-grid');

    if (grid) {
        const createGrid = () => {
            grid.innerHTML = '';

            const tileSize = 60;
            const columns = Math.ceil(window.innerWidth / tileSize);
            const rows = Math.ceil(window.innerHeight / tileSize);

            grid.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;
            grid.style.gridTemplateRows = `repeat(${rows}, 1fr)`;

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

            // Assign offsets to each tile for the coherent glow effect
            const tiles = grid.getElementsByClassName('tile');
            for (let tile of tiles) {
                const rect = tile.getBoundingClientRect();
                tile.style.setProperty('--tile-left', `${rect.left}px`);
                tile.style.setProperty('--tile-top', `${rect.top}px`);
            }
        };

        window.addEventListener('resize', createGrid);
        createGrid();

        // Mouse Tracking on the container
        grid.onmousemove = e => {
            const { clientX, clientY } = e;
            grid.style.setProperty('--mouse-x', `${clientX}px`);
            grid.style.setProperty('--mouse-y', `${clientY}px`);
        };
    }
});
