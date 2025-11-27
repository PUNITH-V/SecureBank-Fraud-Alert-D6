'use client';

import { motion } from 'motion/react';

export const VoiceWaveAnimation = () => {
  return (
    <div className="flex items-center justify-center gap-1.5 h-24">
      {[...Array(5)].map((_, i) => (
        <motion.div
          key={i}
          animate={{
            scaleY: [0.3, 1, 0.3],
            opacity: [0.5, 1, 0.5],
          }}
          transition={{
            duration: 0.8,
            repeat: Infinity,
            ease: "easeInOut",
            delay: i * 0.1,
          }}
          className="w-2 bg-gradient-to-t from-blue-500 via-purple-500 to-pink-500 rounded-full"
          style={{ height: '100%' }}
        />
      ))}
    </div>
  );
};
