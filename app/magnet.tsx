export default function Magnet({ passage }: { passage: string }) {
  const words = passage.split(" ");
  let cumulativeRotation = Math.random() * 2 - 2;
  const rotationVariance = 2;
  const dampingFactor = 2;
  const maxRotation = 3.5;

  return (
    <p className="text-sm mb-4">
      {words.map((word, index) => {
        const randomRotation =
          Math.random() * rotationVariance - rotationVariance / 2;
        const penalizedRotation =
          randomRotation - cumulativeRotation * dampingFactor;
        // Clamp the cumulative rotation between -maxRotation and maxRotation
        cumulativeRotation = Math.min(
          Math.max(cumulativeRotation + penalizedRotation, -maxRotation),
          maxRotation
        );
        return (
          <span
            key={index}
            style={{
              rotate: `${cumulativeRotation}deg`,
              marginRight: `${Math.random() * 8}px`,
              marginBottom: `4px`,
            }}
            className="inline-block p-1 px-2.5 bg-[#e8e8e8] border-t border-l border-[rgba(0,0,0,0.05)] shadow-[0_1px_0_black,1px_0_0_black,1px_2px_0_black,2px_1px_0_black,1px_1px_1px_black] z-10"
          >
            {word}{" "}
          </span>
        );
      })}
    </p>
  );
}
