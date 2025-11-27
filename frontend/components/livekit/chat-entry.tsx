import * as React from 'react';
import { cn } from '@/lib/utils';

export interface ChatEntryProps extends React.HTMLAttributes<HTMLLIElement> {
  /** The locale to use for the timestamp. */
  locale: string;
  /** The timestamp of the message. */
  timestamp: number;
  /** The message to display. */
  message: string;
  /** The origin of the message. */
  messageOrigin: 'local' | 'remote';
  /** The sender's name. */
  name?: string;
  /** Whether the message has been edited. */
  hasBeenEdited?: boolean;
}

export const ChatEntry = ({
  name,
  locale,
  timestamp,
  message,
  messageOrigin,
  hasBeenEdited = false,
  className,
  ...props
}: ChatEntryProps) => {
  const time = new Date(timestamp);
  const title = time.toLocaleTimeString(locale, { timeStyle: 'full' });

  return (
    <li
      title={title}
      data-lk-message-origin={messageOrigin}
      className={cn('group flex w-full flex-col gap-1.5 mb-6', className)}
      {...props}
    >
      <header
        className={cn(
          'flex items-center gap-2 text-sm px-2',
          messageOrigin === 'local' ? 'flex-row-reverse' : 'text-left'
        )}
      >
        {name && <strong className="text-white/90 font-semibold">{name}</strong>}
        <span className="font-mono text-xs text-white/40 opacity-0 transition-opacity ease-linear group-hover:opacity-100">
          {hasBeenEdited && '*'}
          {time.toLocaleTimeString(locale, { timeStyle: 'short' })}
        </span>
      </header>
      <div
        className={cn(
          'relative max-w-[75%] px-5 py-3.5 shadow-xl backdrop-blur-md transition-all duration-300 group-hover:scale-[1.01] group-hover:shadow-2xl',
          messageOrigin === 'local' 
            ? 'ml-auto bg-gradient-to-br from-teal-600 via-cyan-600 to-teal-700 text-white border border-teal-400/40 rounded-[20px] rounded-tr-sm group-hover:border-teal-300/60' 
            : 'mr-auto bg-gradient-to-br from-orange-500/20 to-fuchsia-500/10 text-white border border-orange-400/30 rounded-[20px] rounded-tl-sm group-hover:border-orange-400/50'
        )}
      >
        {/* Speech bubble tail */}
        <div
          className={cn(
            'absolute top-0 w-0 h-0 transition-all duration-300',
            messageOrigin === 'local'
              ? 'right-0 translate-x-0 border-l-[12px] border-l-teal-600 border-t-[12px] border-t-transparent'
              : 'left-0 translate-x-0 border-r-[12px] border-r-orange-500/20 border-t-[12px] border-t-transparent'
          )}
        />
        <p className="text-[15px] leading-relaxed relative z-10">{message}</p>
        
        {/* Shine effect on hover */}
        <div className={cn(
          'absolute inset-0 rounded-[20px] opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none',
          messageOrigin === 'local' 
            ? 'bg-gradient-to-tr from-transparent via-white/10 to-transparent rounded-tr-sm'
            : 'bg-gradient-to-tr from-transparent via-orange-300/10 to-transparent rounded-tl-sm'
        )} />
      </div>
    </li>
  );
};
