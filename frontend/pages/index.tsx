import { useState } from "react";

export default function Home() {
    const [form, setForm] = useState({
        name: "",
        email: "",
        linkedin: "",
        skills: "",
        experiences: "",
        tone: "Formal",
    });

    const [generated, setGenerated] = useState("");
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setGenerated("");

        const prompt = `Summary:
        Name: ${form.name}
        Email: ${form.email}
        LinkedIn: ${form.linkedin}
        Skills: ${form.skills}
        Experiences: ${form.experiences}

        Skills:
        - `;

        try {
            const res = await fetch("http://localhost:8000/generate-resume", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt }),
            });
            const data = await res.json();
            setGenerated(data.resume);
        } catch (error) {
            console.error(error);
            alert("Error generating resume.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gray-100 p-8">
            <div className="max-w-xl mx-auto bg-white p-6 rounded-2xl shadow">
                <h1 className="text-2xl font-bold mb-4">AI Resume Generator</h1>
                <form onSubmit={handleSubmit} className="space-y-3">
                    {Object.keys(form).map((key) =>
                        key !== "tone" ? (
                            <input
                                key={key}
                                type="text"
                                name={key}
                                placeholder={
                                    key.charAt(0).toUpperCase() + key.slice(1)
                                }
                                value={form[key]}
                                onChange={handleChange}
                                className="w-full p-2 border rounded"
                            />
                        ) : (
                            <select
                                key={key}
                                name={key}
                                value={form[key]}
                                onChange={handleChange}
                                className="w-full p-2 border rounded"
                            >
                                <option value="Formal">Formal</option>
                                <option value="Friendly">Friendly</option>
                                <option value="Technical">Technical</option>
                            </select>
                        )
                    )}
                    <button
                        type="submit"
                        disabled={loading}
                        className="bg-blue-600 text-white py-2 px-4 rounded hover:bg-blue-700"
                    >
                        {loading ? "Generating..." : "Generate Resume"}
                    </button>
                </form>

                {generated && (
                    <div className="mt-6">
                        <h2 className="text-xl font-semibold mb-2">
                            Generated Resume:
                        </h2>
                        <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded border overflow-x-auto">
                            {generated}
                        </pre>
                    </div>
                )}
            </div>
        </div>
    );
}
