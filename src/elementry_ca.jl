const start = "..........#.........."
const rules = [90, 30 , 14]

# stolen
rule2poss(rule) = [rule & (1 << (i - 1)) != 0 for i = 1:8]

# robbed
cells2bool(cells) = [cells[i] == '#' for i = 1:length(cells)]

# snatched
bools2cells(bset) = prod([bset[i] ? '#' : '.' for i = 1:length(bset)])

# borrowed
function transform(bset, ruleposs)
	newbset = map(x->ruleposs[x],
		[bset[i - 1] * 4 + bset[i] * 2 + bset[i + 1] + 1
		for i = 2:length(bset)-1])
	vcat(newbset[end], newbset, newbset[1])
end


# mine
function output_rule(rule, gens)
	println("\ndisplaying rule $rule:")
	startset = cells2bool(start)
	bset = vcat(startset[end], startset, startset[1])
	rp = rule2poss(rule)
	for _ = 1:gens
		println(bools2cells(bset[2:end-1])) #clip ends
		bset = transform(bset, rp) #mutate bset
	end
end

# mine
function get_bset(rule, gens)
	arr = []
	startset = cells2bool(start)
	bset = vcat(startset[end], startset, startset[1])
	rp = rule2poss(rule)
	for _ = 1:gens
		append!(arr, bset[2:end-1])
		bset = transform(bset, rp)
	end
	return arr
end

# mine
for rule in rules
	output_rule(rule, 10)
end

# mine
example = get_bset(30, 10)
example = convert(Array{Bool}, example::Any)
println(example)