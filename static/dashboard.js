async function loadNodes() {
    const res = await fetch("/api/status");
    const nodes = await res.json();

    const container = document.getElementById("nodes");
    container.innerHTML = "";

    nodes.forEach(n => {
        if (n.status === "DOWN") {
            fetch(`/api/recover/${n.id}`);
        }

        container.innerHTML += `
        <div class="card">
            <h3>${n.id}</h3>
            <p>Status: <b class="${n.status === 'UP' ? 'ok' : 'fail'}">${n.status}</b></p>
            <p>CPU: ${n.cpu}%</p>
            <p>Memory: ${n.memory}%</p>
            <p>Failure Risk: ${n.prediction}%</p>
        </div>
        `;
    });
}

setInterval(loadNodes, 4000);
loadNodes();
