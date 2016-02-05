lift_max = 1.08;
lift_min = 1.01;
lift_steps = 20;

drag_max = 0.20;
drag_min = 0.14;
drag_steps = 20;

lift = zeros(1, lift_steps);
drag = zeros(1, drag_steps);
times = [];

for i = 1:(lift_steps + 1)
    for j = 1:(drag_steps + 1)
        lifti = lift_min + (i - 1)*(lift_max - lift_min)/lift_steps;
        dragj = drag_min + (j - 1)*(drag_max - drag_min)/drag_steps;
        lift(i) = lifti;
        drag(j) = dragj;
        times(j,i) = simulator([lifti, dragj]);
    end
end

delete(findall(0))
bdclose('all')

surf(lift, drag, times)