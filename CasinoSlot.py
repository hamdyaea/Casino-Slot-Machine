#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Virtual-credit slot machine demonstration; no real-money betting."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
import secrets
import tkinter as tk
from tkinter import ttk

SYMBOLS = ("BAR", "CHERRY", "SEVEN")
STARTING_CREDITS = 100
STAKE = 10

def payout(reels: tuple[str, str, str]) -> int:
    if len(reels) != 3 or any(x not in SYMBOLS for x in reels):
        raise ValueError("Invalid reel symbols")
    if len(set(reels)) == 1:
        return 50
    if len(set(reels)) == 2:
        return 20
    return 0

@dataclass
class Game:
    credits: int = STARTING_CREDITS
    rounds: int = 0

    def spin(self, reels: tuple[str, str, str] | None = None) -> tuple[tuple[str, str, str], int]:
        if self.credits < STAKE:
            raise ValueError("Insufficient virtual credits")
        if reels is None:
            reels = tuple(secrets.choice(SYMBOLS) for _ in range(3))
        reward = payout(reels)
        self.credits += reward - STAKE
        self.rounds += 1
        return reels, reward

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="store_true", help="Play one spin in terminal")
    args = parser.parse_args()
    game = Game()
    if args.text:
        reels, reward = game.spin()
        print(f"{' | '.join(reels)}; payout {reward}; balance {game.credits} virtual credits")
        return
    root = tk.Tk()
    root.title("Slot Machine — Virtual Credits Only")
    root.geometry("470x275")
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Virtual credits only — no real money", font=("sans", 13)).pack(pady=10)
    reels_var = tk.StringVar(value="— | — | —")
    info = tk.StringVar(value=f"Balance: {game.credits} credits | Stake: {STAKE}")
    ttk.Label(frame, textvariable=reels_var, font=("monospace", 18)).pack(pady=10)
    ttk.Label(frame, textvariable=info).pack(pady=10)
    def spin() -> None:
        try:
            reels, reward = game.spin()
            reels_var.set(" | ".join(reels))
            info.set(f"Payout: {reward} | Balance: {game.credits} | Rounds: {game.rounds}")
        except ValueError as exc:
            info.set(str(exc))
    ttk.Button(frame, text="Spin (10 virtual credits)", command=spin).pack(pady=5)
    ttk.Button(frame, text="Reset virtual credits", command=lambda: reset()).pack(pady=5)
    def reset() -> None:
        game.credits, game.rounds = STARTING_CREDITS, 0
        reels_var.set("— | — | —")
        info.set(f"Balance: {game.credits} credits | Stake: {STAKE}")
    root.mainloop()

if __name__ == "__main__":
    main()
