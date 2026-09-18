/**
 * PROJECT FAILSAFE: Enhanced Web Audio API Synthesizer & Visualizer
 */

class SoundSystem {
  constructor() {
    this.ctx = null;
    this.isMuted = false;
    this.isPlayingMorse = false;
    this.activeMorseOscillators = [];
    this.analyser = null;
    this.visualizerAnimationId = null;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
      this.analyser = this.ctx.createAnalyser();
      this.analyser.fftSize = 256;
      this.analyser.connect(this.ctx.destination);
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  playClick() {
    if (this.isMuted) return;
    this.init();
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(800, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(300, this.ctx.currentTime + 0.03);
    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.03);
    osc.connect(gain);
    gain.connect(this.analyser);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.03);
  }

  playSuccess() {
    if (this.isMuted) return;
    this.init();
    const now = this.ctx.currentTime;
    [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.value = freq;
      gain.gain.setValueAtTime(0, now + idx * 0.07);
      gain.gain.linearRampToValueAtTime(0.12, now + idx * 0.07 + 0.02);
      gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.07 + 0.35);
      osc.connect(gain);
      gain.connect(this.analyser);
      osc.start(now + idx * 0.07);
      osc.stop(now + idx * 0.07 + 0.35);
    });
  }

  playError() {
    if (this.isMuted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(130, now);
    osc.frequency.setValueAtTime(90, now + 0.1);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.linearRampToValueAtTime(0.01, now + 0.25);
    osc.connect(gain);
    gain.connect(this.analyser);
    osc.start(now);
    osc.stop(now + 0.25);
  }

  playAlarmSiren() {
    if (this.isMuted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(350, now);
    osc.frequency.linearRampToValueAtTime(900, now + 0.25);
    osc.frequency.linearRampToValueAtTime(350, now + 0.5);
    osc.frequency.linearRampToValueAtTime(900, now + 0.75);
    osc.frequency.linearRampToValueAtTime(350, now + 1.0);
    gain.gain.setValueAtTime(0.2, now);
    gain.gain.linearRampToValueAtTime(0.01, now + 1.2);
    osc.connect(gain);
    gain.connect(this.analyser);
    osc.start(now);
    osc.stop(now + 1.2);
  }

  playMorseSequence(onComplete) {
    this.init();
    if (this.isPlayingMorse) {
      this.stopMorse();
      return;
    }

    this.isPlayingMorse = true;
    this.startCanvasVisualizer();

    const dotDuration = 0.08;
    const dashDuration = dotDuration * 3;
    const pauseSymbol = dotDuration;
    const pauseLetter = dotDuration * 3;
    const pauseWord = dotDuration * 7;
    const freq = 680;

    const morsePattern = "-.. --- -. --- - / ..-. --- .-.. .-.. --- .-- / - .... . / -... .-.. ..- . / .--. .- - ....";
    let curTime = this.ctx.currentTime + 0.2;

    this.activeMorseOscillators = [];

    // Synthesize robotic speech prompt
    if ('speechSynthesis' in window) {
      const utter = new SpeechSynthesisUtterance("Ignore audio anomalies. Proceed directly to the BLUE folder.");
      utter.pitch = 0.65;
      utter.rate = 0.85;
      window.speechSynthesis.speak(utter);
    }

    for (let i = 0; i < morsePattern.length; i++) {
      if (!this.isPlayingMorse) break;
      const char = morsePattern[i];

      if (char === '.' || char === '-') {
        const dur = char === '.' ? dotDuration : dashDuration;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0, curTime);
        gain.gain.linearRampToValueAtTime(0.18, curTime + 0.005);
        gain.gain.setValueAtTime(0.18, curTime + dur - 0.005);
        gain.gain.linearRampToValueAtTime(0, curTime + dur);
        osc.connect(gain);
        gain.connect(this.analyser);
        osc.start(curTime);
        osc.stop(curTime + dur);
        this.activeMorseOscillators.push(osc);
        curTime += dur + pauseSymbol;
      } else if (char === ' ') {
        curTime += pauseLetter;
      } else if (char === '/') {
        curTime += pauseWord;
      }
    }

    const totalDurationMs = (curTime - this.ctx.currentTime) * 1000;
    this.morseTimer = setTimeout(() => {
      this.isPlayingMorse = false;
      this.stopCanvasVisualizer();
      if (onComplete) onComplete();
    }, totalDurationMs);
  }

  stopMorse() {
    this.isPlayingMorse = false;
    this.stopCanvasVisualizer();
    if (this.morseTimer) clearTimeout(this.morseTimer);
    if (this.activeMorseOscillators) {
      this.activeMorseOscillators.forEach(osc => {
        try { osc.stop(); } catch(e) {}
      });
      this.activeMorseOscillators = [];
    }
  }

  startCanvasVisualizer() {
    const canvas = document.getElementById("morse-visualizer");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const analyser = this.analyser;
    const bufferLength = analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);

    const draw = () => {
      if (!this.isPlayingMorse) return;
      this.visualizerAnimationId = requestAnimationFrame(draw);

      analyser.getByteFrequencyData(dataArray);

      ctx.fillStyle = "#04060a";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const barWidth = (canvas.width / bufferLength) * 2.2;
      let x = 0;

      for (let i = 0; i < bufferLength; i++) {
        const barHeight = (dataArray[i] / 255) * canvas.height;
        ctx.fillStyle = `rgb(${dataArray[i]}, 229, 255)`;
        ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
        x += barWidth + 1;
      }
    };
    draw();
  }

  stopCanvasVisualizer() {
    if (this.visualizerAnimationId) {
      cancelAnimationFrame(this.visualizerAnimationId);
      this.visualizerAnimationId = null;
    }
    const canvas = document.getElementById("morse-visualizer");
    if (canvas) {
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#04060a";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = "rgba(0, 229, 255, 0.2)";
      ctx.beginPath();
      ctx.moveTo(0, canvas.height / 2);
      ctx.lineTo(canvas.width, canvas.height / 2);
      ctx.stroke();
    }
  }
}

window.sounds = new SoundSystem();
