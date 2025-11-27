'use client';

import { motion } from 'motion/react';

export const MicAnimation = () => {
  return (
    <div className="relative flex items-center justify-center">
      {/* Outer pulse ring */}
      <motion.div
        className="absolute w-32 h-32 rounded-full bg-blue-500/20"
        animate={{
          scale: [1, 1.3, 1],
          opacity: [0.5, 0.2, 0.5],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      />
      
      {/* Middle pulse ring */}
      <motion.div
        className="absolute w-24 h-24 rounded-full bg-blue-500/30"
        animate={{
          scale: [1, 1.2, 1],
          opacity: [0.6, 0.3, 0.6],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
          delay: 0.2,
        }}
      />

      {/* Microphone icon container */}
      <motion.div
        className="relative z-10 w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-blue-700 flex items-center justify-center shadow-2xl"
        animate={{
          scale: [1, 1.05, 1],
        }}
        transition={{
          duration: 2,
          repeat: Infinity,
          ease: 'easeInOut',
        }}
      >
        <svg
          width="40"
          height="40"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="text-white"
        >
          <path
            d="M12 1C10.8954 1 10 1.89543 10 3V11C10 12.1046 10.8954 13 12 13C13.1046 13 14 12.1046 14 11V3C14 1.89543 13.1046 1 12 1Z"
            fill="currentColor"
          />
          <path
            d="M8 9C8 8.44772 7.55228 8 7 8C6.44772 8 6 8.44772 6 9V11C6 14.3137 8.68629 17 12 17C15.3137 17 18 14.3137 18 11V9C18 8.44772 17.5523 8 17 8C16.4477 8 16 8.44772 16 9V11C16 13.2091 14.2091 15 12 15C9.79086 15 8 13.2091 8 11V9Z"
            fill="currentColor"
          />
          <path
            d="M12 19C12.5523 19 13 19.4477 13 20V22C13 22.5523 12.5523 23 12 23C11.4477 23 11 22.5523 11 22V20C11 19.4477 11.4477 19 12 19Z"
            fill="currentColor"
          />
          <path
            d="M8 22C8 21.4477 8.44772 21 9 21H15C15.5523 21 16 21.4477 16 22C16 22.5523 15.5523 23 15 23H9C8.44772 23 8 22.5523 8 22Z"
            fill="currentColor"
          />
        </svg>
      </motion.div>
    </div>
  );
};
