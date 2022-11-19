const {subtle} = globalThis.crypto;


const calculate_hash = async (input) => {
    const [result, counter_start, data] = input.split(":")
    let hash_result = ""
    let counter = parseInt(counter_start)
    console.log(counter)
    // throw "a"
    const start = performance.now()

    while (hash_result !== result) {
        const msgBuffer = new TextEncoder().encode(`${counter}:${data}`);
        // const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
        const hashBuffer = await subtle.digest('SHA-256', msgBuffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        hash_result = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        console.log(counter)
        counter = counter +1
    }
    console.log("Time taken:", performance.now() - start)
    return `${result}:${counter - 1}:${data}`;
}


await calculate_hash("78916a39f3fb9950befce6efb5dce63d80be5036361c95fea6697a19617a8f0e:42965:a922618641d6bcc3a7d02a39")