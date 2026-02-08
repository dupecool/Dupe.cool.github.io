// Initialize Lucide icons
lucide.createIcons();

// Tile Grid Logic
const grid = document.getElementById('tile-grid');

if (grid) {
    // Track mouse for radial glow
    document.addEventListener('mousemove', (e) => {
        grid.style.setProperty('--mouse-x', `${e.clientX}px`);
        grid.style.setProperty('--mouse-y', `${e.clientY}px`);
    });

    function createGrid() {
        grid.innerHTML = '';

        const tileSize = 50;
        const columns = Math.ceil(window.innerWidth / tileSize);
        const rows = Math.ceil(window.innerHeight / tileSize);

        grid.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;

        const totalTiles = columns * rows;

        // Limit total tiles to prevent lag on very large screens
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
}
