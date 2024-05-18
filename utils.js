function regEx(value) {
    return value
    .replace(/[\n\r\t]+/g, ' ')
    .replace(/\s+/g, ' ')
    .replace(/"/g, "'")
    .trim();
}

module.exports = { regEx };