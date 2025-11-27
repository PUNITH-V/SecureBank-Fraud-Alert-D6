'use client';

import { motion } from 'motion/react';

export const TypingIndicator = () => {
  return (
    <div className="flex items-center gap-2 px-5 py-4 max-w-[75%] mr-auto bg-gradient-to-br from-white/15 to-white/5 text-white border border-white/30 rounded-[20px] rounded-tl-sm backdrop-blur-md shadow-xl">
      <div className="flex gap-1.5">
        {[0, 1, 2].map((i) => (
          <motion.div
            key={i}
            animate={{
              y: [0, -8, 0],
              opacity: [0.5, 1, 0.5],
            }}
            transition={{
              duration: 0.8,
              repeat: Infinity,
              ease: "easeInOut",
              delay: i * 0.15,
            }}
            className="w-2.5 h-2.5 bg-white/60 rounded-full"
          />
        ))}
      </div>
      <span className="text-sm text-white/60 ml-2">AI is thinking...</span>
    </div>
  );
};
