'use client';

import { motion } from 'motion/react';

export const LoadingDots = () => {
  return (
    <div className="flex items-center gap-1.5">
      {[0, 1, 2].map((i) => (
        <motion.div
          key={i}
          animate={{
            scale: [1, 1.3, 1],
            opacity: [0.4, 1, 0.4],
          }}
          transition={{
            duration: 1,
            repeat: Infinity,
            ease: "easeInOut",
            delay: i * 0.2,
          }}
          className="w-2 h-2 bg-white/60 rounded-full"
        />
      ))}
    </div>
  );
};
