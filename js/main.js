// Initialize Lucide icons
if (window.lucide) {
    lucide.createIcons();
}

// Tile Grid Logic
const grid = document.getElementById('tile-grid');
const mouseGlow = document.createElement('div');
mouseGlow.id = 'mouse-glow';
document.body.appendChild(mouseGlow);

let tiles = [];

function createGrid() {
    grid.innerHTML = '';
    tiles = [];

    const tileSize = 60;
    const columns = Math.ceil(window.innerWidth / tileSize);
    const rows = Math.ceil(window.innerHeight / tileSize);

    grid.style.gridTemplateColumns = `repeat(${columns}, 1fr)`;

    const totalTiles = columns * rows;
    const maxTiles = 2500; // Cap as per memory
    const finalCount = Math.min(totalTiles, maxTiles);

    const fragment = document.createDocumentFragment();
    for (let i = 0; i < finalCount; i++) {
        const tile = document.createElement('div');
        tile.classList.add('tile');
        fragment.appendChild(tile);
        tiles.push(tile);
    }
    grid.appendChild(fragment);
}

// Mouse tracking for radial glow and tile activation
window.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;

    // Update mouse glow position
    mouseGlow.style.left = `${clientX}px`;
    mouseGlow.style.top = `${clientY}px`;
    mouseGlow.style.opacity = '1';

    // Activate tiles under/near mouse
    // Using simple hover for efficiency, but we can also do distance-based if needed.
    // However, the memory mentioned "cursor-following radial glow" AND "interactive background".
    // If we want tiles to light up as the mouse passes by:
});

// Since tiles have pointer-events, we can use mouseover on the grid
grid.addEventListener('mouseover', (e) => {
    if (e.target.classList.contains('tile')) {
        const tile = e.target;
        tile.classList.add('active');

        // Remove active class after some time to trigger fade out
        setTimeout(() => {
            tile.classList.remove('active');
        }, 50); // Short time to be "active" then transition handles the rest
    }
});

window.addEventListener('resize', createGrid);
createGrid();

// Hide mouse glow when mouse leaves window
document.addEventListener('mouseleave', () => {
    mouseGlow.style.opacity = '0';
});
