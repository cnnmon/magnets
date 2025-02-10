"use client";
import { useEffect, useState } from "react";
import Magnet from "./magnet";

type SearchResult = {
    distance: number;
    passage: string;
};

export default function Home() {
    const [query, setQuery] = useState("");
    const [searchResult, setSearchResult] = useState<Array<SearchResult>>([]);

    useEffect(() => {
        fetch(`/api/query?query=${query || "i am"}`)
            .then((res) => res.json())
            .then((data) => {
                if (data.success) {
                    setSearchResult(data.results);
                }
            });
    }, [query]);

    return (
        <main className="p-20 space-y-4 max-w-2xl mx-auto">
            <textarea
                className="w-full h-10 p-2 border border-gray-300 resize-none text-sm"
                placeholder="do you have original thoughts?"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <div>
                {searchResult.map(({ passage }, index) => (
                    <Magnet key={index} passage={passage} />
                ))}
            </div>
        </main>
    );
}
