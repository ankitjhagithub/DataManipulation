%This contain the extraction of data from the NYUv2 dataset  from its
%original site
work = load('nyu_depth_v2_labeled.mat');
[rows, cols ,channels, num] = size(work.images);

% for i = 1:num
%     temp = work.depths(:,:,i)/max(max(work.depths(:,:,i)));
%     s = strcat('depth_images/',int2str(i), '_depth.jpg');
%     imwrite(temp, s, 'jpg');
% end

% for i = 1:num
%     s = strcat('images/',int2str(i), '_img.jpg');
%     imwrite(work.images(:,:,:,i), s, 'jpg');
% end

for i = 1:num
    s = strcat('labels_gray/',int2str(i), '_label.jpg');
    %imwrite(ind2rgb(im2unit8(mat2gray(work.labels(:,:,i))),parula(256)),s,'jpg')
    imwrite(im2uint8(mat2gray(work.labels(:,:,i))), s, 'jpg')
    %imwrite(work.labels(:,:,i), s, 'jpg');
end
