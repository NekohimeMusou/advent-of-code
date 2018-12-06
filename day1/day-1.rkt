#lang racket

; Name of the input file
(define INPUT-FILENAME "input.txt")

; Read each line from an input port into a list
(define (lines->list input)
  (for/list ([line (in-lines input)])
    line))

; Read the lines from our input file into a list
(define lines (call-with-input-file INPUT-FILENAME
                                    lines->list))

; Iterate the list, convert to numbers, and add them into
; an accumulator. We don't need to do anything about the +s
(define (calc-final-freq freq-list)
  (for/fold ([freq 0])
            ([delta-str (in-list freq-list)])
    
    (define delta (string->number delta-str))
    (+ freq delta)))

(define (calc-first-nth-freq freq-list n)
  (for/fold ([freq-table #hasheq()]
             [current-freq 0]
             #:break ()
             #:result current-freq)
            ([freq (in-list freq-list)])
    ))
; Call the function with our list
(define final-frequency (calc-final-freq lines))

; Print the frequency all neat-like
(printf "Frequency at end of file: ~a" final-frequency)