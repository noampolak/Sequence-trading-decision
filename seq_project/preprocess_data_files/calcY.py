def YDateAndInd(y_file,wanted_yield):
  c = csv2cell(y_file,1);
 %change dates to numbers
  dates = cellfun(@datenumwarp , c(:,1),"UniformOutput", false);
  %c = [dates, c(:, 2:end)];
  %change numstrings to double
  [row,col] = size(c);
  numbers = cellfun(@str2doublewarp , c(:,2:col-2),"UniformOutput", false);
  present_char = strrep(c(:,col), "%","");
  change_num = str2double(present_char);
  c = [dates, numbers, num2cell(change_num)];
  c = cell2mat(c);
% we asume that the the source file has first row - title, first column is date
%nad last is the yield
   [row,col] = size(c);
   c = [c(:,1),c(:,col)];
   c =sortrows(c);
   yieldArray = findLongY(5, wanted_yield*100, c(:,2));
   y_date_and_ind = [c(:,1),yieldArray];
return y_date_and_ind