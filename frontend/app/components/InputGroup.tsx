interface Props {
  label: string;
  name: string;
  value: any;
  placeholder?: string;
  onChange: (e: any) => void;
}

export default function InputGroup({
  label,
  name,
  value,
  placeholder,
  onChange,
}: Props) {
  return (
    <div className="flex flex-col gap-2">
      <label className="text-gray-300 font-medium">{label}</label>
      <input
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className="input-base"
      />
    </div>
  );
}
