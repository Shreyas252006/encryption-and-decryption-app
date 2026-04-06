function send(action) {
    const form = document.getElementById("form");
    const formData = new FormData(form);

    const url = action === "encrypt" ? "/encrypt" : "/decrypt";

    document.getElementById("status").innerText = "Processing...";

    fetch(url, {
        method: "POST",
        body: formData
    })
    .then(res => {
        // ❗ Important: detect backend errors (like 404)
        if (!res.ok) {
            throw new Error("Server error: " + res.status);
        }

        const disposition = res.headers.get("Content-Disposition");
        let filename = "output";

        if (disposition && disposition.includes("filename=")) {
            filename = disposition.split("filename=")[1].replace(/"/g, "");
        }

        return res.blob().then(blob => ({ blob, filename }));
    })
    .then(({ blob, filename }) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = filename;
        a.click();

        document.getElementById("status").innerText = "Done ✅";
    })
    .catch(err => {
        document.getElementById("status").innerText = "Error ❌";
        console.error(err);
    });
}