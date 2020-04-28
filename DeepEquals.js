/**
Write a function deepEqual that takes two values and returns true only if they are the 
same value or are objects with the same properties, where the values of the properties
are equal when compared with a recursive call to deepEqual.

To find out whether values should be compared directly (use the === operator for that)
or have their properties compared, you can use the typeof operator. If it produces an 
"object" for both values, you should do a deep comparison. But you have to take one 
silly exception into account: because of a historical accident, typeof null also produces "object".

The Object.keys function will be useful when you need to go over the properties of objects to compare them.
*/

function deepEqual(st1, st2) {
	if(typeof st1 === 'object' && typeof st2 === 'object' && st1 != null && st2 != null) {
		const keys1 = Object.keys(st1);
		const keys2 = Object.keys(st2);
		if (keys1.length === keys2.length) {
			let count = 0;
			for (let i = 0; i < keys1.length; i++) {
				if (typeof st1[keys1[i]] === 'object' && typeof st2[keys2[i]] === 'object') {
					return deepEqual(st1[keys1[i]], st2[keys2[i]])
				}
				else if (st1[keys1[i]] === st2[keys2[i]]) {
					count++;
				}
				else {
					return false;
				}
			}
			if (count === keys1.length) {
				return true;
			} else {
				return false;
			}
		} else  {
			return false;
		}
	} else if (st1 == st2) {
		return true;
	} else {
		return false;
	}
}

var obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
console.log(deepEqual(obj, {here: 1, object: 2}));
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
console.log(deepEqual(obj, {here: {is: "an"}, object: {is: "an"}}));
