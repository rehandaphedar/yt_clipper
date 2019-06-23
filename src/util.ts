export async function retryUntilTruthyResult<R>(fn: () => R, wait = 100) {
  let result: R = fn();
  while (!result) {
    console.log(`Retrying function: ${fn.name} because result was ${result}`);
    result = fn();
    await sleep(wait);
  }
  return result;
}

export function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export function once(fn: Function, context: any) {
  var result: Function;
  return function() {
    if (fn) {
      result = fn.apply(context || this, arguments);
      fn = null;
    }
    return result;
  };
}

export function setAttributes(el: HTMLElement, attrs: {}) {
  Object.keys(attrs).forEach((key) => el.setAttribute(key, attrs[key]));
}

export function copyToClipboard(str: string) {
  const el = document.createElement('textarea');
  el.value = str;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}

export function clampNumber(number: number, min: number, max: number) {
  return Math.max(min, Math.min(number, max));
}

export function toHHMMSS(seconds: number) {
  return new Date(seconds * 1000).toISOString().substr(11, 12);
}

export function toHHMMSSTrimmed(seconds: number) {
  return toHHMMSS(seconds).replace(/(00:)+(.*)/, '$2');
}
